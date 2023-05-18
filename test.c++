#include <iostream>
using namespace std;
int main() {
    int a = 1;
    int b = 7;
    int tmp = 0;
    tmp = a; 
    a = b;
    b = tmp;
    cout << a;
    cout << b;
    return 0;
}