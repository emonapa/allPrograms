/*
This program generates all possible combinations of letters
based on the provided input number using the CartesianProduct() function.
These combinations are stored in the results[] array.
The program then parses a text file
containing a list of names and phone numbers,
searching for uninterrupted sequences of the same characters
in names or uninterrupted sequences of digits in phone numbers.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#define MAX_RESULTS 65536 // Maximum number of results in cartesian product.
#define MAX_RESULT_LEN 8 // Maximum length of individual result.

void CartesianProduct(char *input, char results[MAX_RESULTS][MAX_RESULT_LEN], int *output_count) {
    char *letters[] = {"+", "", "abc", "efg", "ihj", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    //                  0    1    2      3      4      5      6      7       8      9

    int num_len = strlen(input);
    int new_num_len = 0;
    int num_conv_array[MAX_RESULT_LEN] = {0};

    for (int i = 0; i < num_len; i++) {
        int digit = input[i] - '0';
        if (digit != 1) {
            num_conv_array[new_num_len] = digit;
            new_num_len++;
        }
    }

    if (new_num_len < 1 || new_num_len > MAX_RESULT_LEN) {
        //8 because of MAX_RESULT (4^8 - 1)
        printf("Invalid number of digits. Must be less than 9 (digit one doesn't count).\n");
        return;
    }

    int output_index = 0;
    int indices[MAX_RESULT_LEN] = {0};

    while (1) {
        for (int i = 0; i < new_num_len; i++) {
            int digit = num_conv_array[i];
            results[output_index][i] = letters[digit][indices[i]];
        }
        results[output_index][new_num_len] = '\0';

        int carry = 1;
        for (int i = new_num_len - 1; i >= 0; i--) {
            int digit = num_conv_array[i];
            int letter_count = strlen(letters[digit]);

            indices[i] += carry;
            carry = indices[i] / letter_count;
            indices[i] %= letter_count;

            if (carry == 0) {
                break;
            }
        }

        if (carry) {
            break;
        }
        output_index++;
    }
    *output_count = output_index;
}


int FindMatches(char *input, char results[MAX_RESULTS][MAX_RESULT_LEN], int *output_count){
  FILE *file = fopen("seznam.txt", "r");
    if (file == NULL) {
        perror("Failed to open file.");
        return 1;
    }

    char name_holder[100];
    char phone_number[100];
    int matches_count = 0;

    while (fgets(name_holder, sizeof(name_holder), file) && fgets(phone_number, sizeof(phone_number), file)) {
        int len = strlen(name_holder);
        if (len > 0 && name_holder[len - 1] == '\n') {
            name_holder[len - 1] = '\0';
        }

        len = strlen(phone_number);
        if (len > 0 && phone_number[len - 1] == '\n') {
            phone_number[len - 1] = '\0';
        }

        for (int i = 0; name_holder[i]; i++) { // name_holder[i] <=> name_holder[i] != '\0'
            name_holder[i] = tolower(name_holder[i]);
        }
        
        if (strstr(phone_number, input) != NULL) {
            printf("%s, %s\n", name_holder, phone_number);
            matches_count++;
        }
        else {
            for (int i = 0; i < *output_count; i++){
                if (strstr(name_holder, results[i]) != NULL) {
                    printf("%s, %s\n", name_holder, phone_number);
                    matches_count++;
                    break;
                }
            }
        }
    }
    if (matches_count == 0){
        printf("No contacts found.");
    }
    fclose(file);
}


int WriteAllContacts(){
    FILE *file = fopen("seznam.txt", "r");
    if (file == NULL) {
        perror("Failed to open file.");
        return 1;
    }

    char name_holder[100];
    char phone_number[100];

    while (fgets(name_holder, sizeof(name_holder), file) && fgets(phone_number, sizeof(phone_number), file)) {
        int len = strlen(name_holder);
        if (len > 0 && name_holder[len - 1] == '\n') {
            name_holder[len - 1] = '\0';
        }

        len = strlen(phone_number);
        if (len > 0 && phone_number[len - 1] == '\n') {
            phone_number[len - 1] = '\0';
        }

        printf("%s, %s\n", name_holder, phone_number);
    }
    fclose(file);
}

bool IsAllDigits(const char *input) {
    for (int i = 0; i < strlen(input); i++) {
        if (input[i] < '0' || input[i] > '9') {
            return false;
        }
    }
    return true;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        WriteAllContacts();
        return 1;
    }

    char *input = argv[1];

    if (!IsAllDigits(input)) {
        printf("Invalid input: %s.", input);
        return 1;
    }

    char results[MAX_RESULTS][MAX_RESULT_LEN];
    int output_count = 0;

    CartesianProduct(input, results, &output_count);
    if (&output_count != 0) {
        FindMatches(input, results, &output_count);
    }

    return 0;
}

