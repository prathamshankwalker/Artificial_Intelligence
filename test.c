// #include <stdio.h>
// #include <string.h>

// #define MAX_LEN 1000

// int main() {
//     char original_data[MAX_LEN];
//     char flag[MAX_LEN];
//     char stuffed_data[MAX_LEN];
//     char destuffed_data[MAX_LEN];
//     int i, j;

//     // Input data and flag
//     printf("Enter data string : ");
//     fgets(original_data, MAX_LEN, stdin);
//     printf("Enter flag data stream : ");
//     fgets(flag, MAX_LEN, stdin);

//     // Remove newline characters from input strings
//     original_data[strcspn(original_data, "\n")] = 0;
//     flag[strcspn(flag, "\n")] = 0;

//     // Bit stuffing
//     j = 0;
//     for (i = 0; i < strlen(original_data); i++) {
//         stuffed_data[j++] = original_data[i];
//         if (original_data[i] == '1') {
//             int count = 1;
//             while (i+1 < strlen(original_data) && original_data[i+1] == '1') {
//                 count++;
//                 i++;
//                 if (count == 5) {
//                     stuffed_data[j++] = '0';
//                     count = 0;
//                 }
//             }
//             if (count == 4) {
//                 stuffed_data[j++] = '0';
//             }
//         }
//     }
//     stuffed_data[j] = '\0';

//     // Add flag at the beginning and end of stuffed data
//     strcpy(destuffed_data, &stuffed_data[strlen(flag)]);
//     destuffed_data[strlen(destuffed_data) - strlen(flag)] = '\0';

//     // Bit destuffing
//     j = 0;
//     for (i = 0; i < strlen(destuffed_data); i++) {
//         destuffed_data[j++] = destuffed_data[i];
//         if (destuffed_data[i] == '1') {
//             int count = 1;
//             while (i+1 < strlen(destuffed_data) && destuffed_data[i+1] == '1') {
//                 count++;
//                 i++;
//                 if (count == 5) {
//                     i++;
//                     count = 0;
//                 }
//             }
//             if (count == 4) {
//                 i++;
//             }
//         }
//     }
//     destuffed_data[j] = '\0';

//     // Output stuffed and destuffed data
//     printf("After bit stuffing: %s\n", stuffed_data);
//     printf("Data sent by sender: %s%s%s\n", flag, stuffed_data, flag);
//     printf("Data received after destuffing: %s\n", destuffed_data);

//     return 0;
// }
// // #output 
// // # Enter data string : 01111101111110
// // # enter flag data stream : 01111110
// // # after bit stuffing 0111110011111010
// // # data sent by sender is  01111110011111001111101001111110
// // # data received after destuffing :  01111101111110
// `