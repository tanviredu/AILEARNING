#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Define constants 
#define MAX_URLS 100
#define MAX_LENGTH 256
#define SHORT_LEN 6

// In-memory database
char urls[MAX_URLS][MAX_LENGTH];
char short_codes[MAX_URLS][SHORT_LEN + 1];
int url_count = 0;

// Function to get original URL from the short code
void get_original_url() {
    char input_short[SHORT_LEN + 1];
    printf("Enter the Short URL: ");
    scanf("%s", input_short);  // Read short URL
    
    int i;
    for (i = 0; i < url_count; i++) {
        if (strcmp(short_codes[i], input_short) == 0) {  // Fix: compare strings correctly
            printf("Original URL: %s\n", urls[i]);
            return;
        }
    }
    printf("Short URL not found\n");
}

// Function to generate a short code
void generate_short_code(char short_code[]) {
    char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    int i;
    for (i = 0; i < SHORT_LEN; i++) {
        int index = rand() % (sizeof(charset) - 1);
        short_code[i] = charset[index];
    }
    short_code[SHORT_LEN] = '\0';  // Null-terminate the string
}

// Function to shorten the URL
void shorten_url() {
    if (url_count >= MAX_URLS) {
        printf("URL Database is full. Cannot shorten more URLs.\n");
        return;
    }

    printf("Enter URL to shorten: ");
    scanf(" %[^\n]", urls[url_count]);  // Read URL including spaces

    // Generate a short code
    generate_short_code(short_codes[url_count]);

    printf("Shortened URL: %s\n", short_codes[url_count]);
    url_count++;
}

// Main function
int main() {
    int choice;
    while (1) {
        // Display the menu
        printf("\nSimple URL Shortener\n");
        printf("1. Shorten URL\n");
        printf("2. Get Original URL\n");
        printf("3. Exit\n");
        printf("Choose your option => ");

        // Read user input (choice)
        scanf("%d", &choice);
        getchar();  // Clear the newline character left by scanf

        if (choice == 1) {
            shorten_url();  // Shorten URL
        } else if (choice == 2) {
            get_original_url();  // Get the original URL from short code
        } else if (choice == 3) {
            printf("Exiting...\n");
            break;  // Exit the program
        } else {
            printf("Invalid choice! Try again.\n");
        }
    }
    return 0;
}
