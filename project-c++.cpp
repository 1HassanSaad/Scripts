#include <iostream>
#include <windows.h>
using namespace std;
void fig1(int a);
void fig2(int b);
void fig3(int c);
int main()
{
    int x,n;
    cout<<"enter number of figure : ";
    cin>>x;
    cout<<"enter size = ";
    cin>>n;
    if(x==1){
        fig1(n);
    }
    else if(x==2){
        fig2(n);
    }
    else if(x==3){
        fig3(n);
    }
    else {
        cout<<"try again.";
    }
    return 0;
}
void fig1(int a){
    int i,j,h,c,s;
    system("cls");
    for(i=1;i<=a;i++){
        for(j=1;j<=a-i;j++)
            cout<<" ";
        for(h=1;h<=i;h++)
            cout<<"*";
        cout<<endl;
    }
    Sleep(500);
    system("cls");
    for(i=1;i<=75/a-1;i++){
        for(s=1;s<=a;s++){
            for(c=1;c<=a*i;c++)
                cout<<" ";
            for(j=1;j<=a-s;j++)
                cout<<" ";
            for(h=1;h<=s;h++)
                cout<<"*";
            cout<<endl;
        }
            Sleep(500);
            system("cls");
    }
}
void fig2(int b){
    int i,j,s,c,h;
    system("cls");
    for(i=1;i<=b;i++){
        for(j=1;j<=b;j++)
            cout<<"*";
        cout<<endl;
    }
    Sleep(500);
    system("cls");
    for(i=1;i<=55/b-1;i++){
        for(s=1;s<=b*i;s++){
            for(c=1;c<=b;c++)
                cout<<" ";
            cout<<endl;
        }
        for(s=1;s<=b;s++){
            for(h=1;h<=b;h++)
                cout<<"*";
            cout<<endl;
        }
            Sleep(500);
            system("cls");
    }
    }
void fig3(int c){
    int i,j,s,x,z,h;
    system("cls");
    for(i=1;i<=c;i++){
        for(j=1;j<=i;j++)
            cout<<"*";
        cout<<endl;
    }
    Sleep(500);
    system("cls");
    for(i=1;i<=55/c-1;i++){
        for(s=1;s<=c*i;s++){
            for(x=1;x<=c;x++)
                cout<<" ";
            cout<<endl;
        }
        for(z=1;z<=c;z++){
            for(x=1;x<=c*i;x++)
                cout<<" ";
            for(h=1;h<=z;h++)
                cout<<"*";
            cout<<endl;
        }
            Sleep(500);
            system("cls");
    }
    }
