#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <lcd.h>
#include <unistd.h>

int main(int argc, char **argv) {
    int fd;
    int c;
    int i;

    if(wiringPiSetupGpio() == -1) {
        printf("Setup Fail\n");
        exit(1);
    }
    fd = lcdInit(2,16,4,14,15,23,24,25,8,0,0,0,0);

    lcdClear(fd);
    lcdPuts(fd,"ABCDEFGHIJKLMNOP");
    lcdPosition(fd,0,1);
    lcdPuts(fd,"abcdefghijklmnop");

    while (1){
        printf("0:lcdDisplay test\n");
        printf("1:lcdCursor test\n");
        printf("2:lcdBlink test\n");
        printf("q:End\n");
        c=getchar();
        if(c == 'q') break;

        if(c == '0') {
            for(i=0;i<10;i++) {
                lcdDisplay(fd,0);
                sleep(1);
                lcdDisplay(fd,1);
                sleep(1);
            }
        }

        if(c == '1') {
            for(i=0;i<16;i++){
                lcdPosition(fd,i,0);
                lcdCursor(fd,1);
                sleep(1);
            }
            lcdCursor(fd,0);
        }

        if(c == '2') {
            for(i=0;i<16;i++){
                lcdPosition(fd,i,1);
                lcdCursorBlink(fd,1);
                sleep(1);
            }
            lcdCursorBlink(fd,0);
        }
    }
    lcdClear(fd);
}