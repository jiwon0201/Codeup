#include <stdio.h>

int A, B, C, i, x, y, a[10000]={}, b[10000]={}, r[10000]={}, q[10000]={};



int gcd(int a, int b) {
   if (b == 0) return a;
   else return gcd(b, a%b);}


int main(){
    scanf("%d %d %d", &A, &B, &C);
    
    int s[] = {A>0 ? 1:-1, B>0 ? 1:-1 , A>B};    
    
    //0이 포함된 경우
    if (A==0 && B!=0){
        if(C/B*B == C) {x=1; y=C/B; goto answer;}
        else goto no_answer;}
    else if(B==0 && A!=0){
        if(C/A*A == C) {x = C/A; y=1; goto answer;}
        else goto no_answer;}
    else if(A==0 && B==0){
        if(C) goto no_answer;
        else {x=1 ; y=1; }goto answer;}//1들은 다 임의의 수 - 정답으로 인정
    
    //부호
    
    
    A *= s[0];
    B *= s[1];
    
    int GCD = gcd(A,B);//최대공약수
    
    
    //점화식 가동
    if(s[2]){r[0] = A; r[1] = B;}//A>B
    else {r[0] = B ; r[1] = A;}
    
    for(i=1 ; r[i]!=0 ; i++){
        q[i] = r[i-1]/r[i];
        r[i+1] = r[i-1]%r[i];}
        
    int n=i-1;
    
    if(C%GCD) goto no_answer;//디오판토스 방정식 해가 없는 경우
    
    a[n] = -q[n-1]; b[n] = 1;
    for(i=n-1 ; i>=1 ; i--){
        a[i] = b[i+1] - q[i-1]*a[i+1];
        b[i] = a[i+1];}
    
    
    int t = C/GCD;
    
    //출력부
    if(s[2]){
        x = t*a[1]*s[0]; y = t*b[1]*s[1];}
    else{
        x = t*b[1]*s[0]; y = t*a[1]*s[1];}
    
    answer:    
    printf("%d %d",x ,y );
    return 0;
    
    
    no_answer:
        printf("Not Exist");
    
    
}
