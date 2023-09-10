#include <stdio.h>
#define ROWS 2 
#define LEN 3
int add(int a,int b){
    int c;
    c = a + b;
    return c;
}

void testPrint(float v){
    printf("%.2f",v);
    return;
}
int main()
{   
    //testPrint(1.5);
    /*int m=6,n=2;
    int c;
    c = add(m,n);
    printf("%d\n",c);*/

    /*
    int maze[ROWS][LEN] = {{1,2,3},
                           {4,5,6}};
    int i,j;
    for (i = 0; i < ROWS; i++){
        for (j = 0; j <LEN;j++){
            printf("%d\t",maze[i][j]);
        }
        printf("\n");
    }*/
    
    
    /*int number[5] = {0,1,2,3,4};
    int len = sizeof(number) / sizeof(number[0]);
    printf("%d\n",len);
    for (int i = 0; i < len;i++){
      printf("%d ",number[i]);  
    }*/
    
    /*int score = 0;
    int sum = 0;
    for (int i = 0; i < 5; i++){
        printf("輸入分數:");
        scanf("%d",&score);
        if (score < 0 || score > 100){
            printf("分數錯誤\n");
            continue;
        }
        sum += score;
    }
    printf("sum:%d",sum);*/
    
   /* for(int i =1; i <= 10; i++){
        if (i == 7){
            //break;
            continue;
        }
        printf("%d ",i);
    }*/

/*int score = 0;
    int sum = 0;
    int count = -1;
    while(score != -1){
    count++;    
    sum += score;
    printf("請輸入分數(-1結束):");
    scanf("%d",&score);
    }
    printf("sum:%d",sum);*/
    
    /*for (int i =1; i <= 9; i++){
        for (int k = 1; k <=9; k++){
            printf(" %d*%d=%2d",i,k,i * k);
        }
        printf("\n");
    }*/
    
    /*for ( int i = 1; i <= 10;i++){
        printf("%d ",i);
    }*/
    
   /* int action = 0;
    printf("1 Play\n");
    printf("2 Stop\n");
    printf("3 Exit\n");
    printf("4 Clear\n");
    printf("5 Pause\n");
    scanf("%d",&action);
    switch(action){
        case 1:
        printf("Play");
        break;
        case 2:
        printf("Stop");
        break;
        case 3:
        printf("Exit");
        break;
        case 4:
        printf("Clear\n");
        case 5:
        printf("Pause\n");
        break;
        default:
         printf("Error");
        break;
    }*/
   /* int score = 0;
    printf("請輸入成績");
    scanf("%d",&score);
    if (score >= 90){
        printf("A");
    }else if(score >= 80 && score < 90){
       printf("B");  
    }else if(score >= 70 && score < 80){
       printf("C");  
    }else if(score >= 60 && score < 70){
        printf("D");
    }else{
        printf("F");
    }*/
    
    /*int score = 0;
    printf("輸入成績:");
    scanf("%d",&score);
    printf("是否及格?%c",score >= 60 ? 'Y' : 'N');
    printf("是否為奇數?%c",score%2 == 1 ? 'Y' : 'N');*/
    
    // "Y" if score >= 60 else "N" python 
     /*int input = 0;
    int remain = 0;
    printf("請輸入整數");
    scanf("%d",&input);
    remain = input % 2;
    if (remain == 1){
        printf("奇數");
    }else{
        printf("偶數");
    }*/
        
    
    /*
    int v1 = 1;//true
    int v2 = 0;//false
    printf("AND %d\n",v1 && v2);
    int v3 = 0;
    int v4 = 1;
    printf("OR %d\n",v1 || v2);
    
    printf("Not %d\n",!v4);*/
    
   /* int a = 1;
    ++a;//a = a + 1
    printf("%d",a);*/
    
    
    /*int input1;
    float input2;
    char input3[10];
    printf("輸入整數\n");
    scanf("%d",&input1);
    printf("My Int:%d\n",input1);
    
    printf("請輸入浮點數\n");
    scanf("%f",&input2);
    printf("My Float:%.2f\n",input2);
    
    printf("請輸入文字:");
    scanf("%10s",&input3);
    printf("My Str:%s",input3);*/
    
    /*printf("Test1:%c\n",'A');
    printf("Test2:%d\n",'A');
    int var1 = 10;
    printf("Test3:%d",var1);*/
    return 0;
}