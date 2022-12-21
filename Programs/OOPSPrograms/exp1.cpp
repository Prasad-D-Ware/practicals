// Implement a class Complex which represents the Complex Number data
// CO1,
// type. Implement the following
// 1. Constructor (including a default constructor which creates the complex CO2 number 0+0i).
// 2. Overload operator + to add two complex numbers.
// 3. Overload operator * to multiply two complex numbers.
// 4. Overload operators << and >> to print and read Complex Numbers.


#include<iostream>
using namespace std;
class complex
{
  double re;
  double img;
 public:
       complex()
       {
        re=0;
        img=0;
       }
friend istream &operator>>(istream &input,complex &c)
{
 cout<<"Enter real part:";
 input>>c.re;
 cout<<"Enter imaginary part:";
 input>>c.img;
 return input;
 
}
friend ostream &operator<<(ostream &output,complex &c)
{
 output<<c.re<<"+"<<c.img<<"i";
 return output;
}
complex operator + (complex c2)
{
 complex c3;
 c3.re=re+c2.re;
 c3.img=img+c2.img;
 return c3;
}
complex operator * (complex c2) 
{
 complex c4;
 c4.re=(re*c2.re)-(img*c2.img);
 c4.img=(img*c2.re)+(re*c2.img);
 return c4;
}
};

int main()
{
 complex c1,c2,c3,c4;
 cout<<"Default constructor value=";
 cout<<c1<<endl;
 cout<<"Enter 1st Complex Number: "<<endl;
 cin>>c1;
  cout<<"Enter 2nd Complex Number: "<<endl;
 cin>>c2;
 c3=c1+c2;
 c4=c1*c2;
 cout<<"The Addition is: "<<c3<<endl;
 cout<<"The Multiplication is: "<<c4<<endl;
 return 0;
}
