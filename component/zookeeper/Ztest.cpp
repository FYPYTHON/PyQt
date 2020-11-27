#include<iostream>
#define DEL_PTR( p ) if(p) delete p; p = NULL;
class A{
    private:
        class B;
        B *b;
    public:
        A();
        ~A();
    public:
        B* getb(){return b;};
        void print();
};
class A::B
{
    public:
        int num;
        void print();

};
A::A(){
    b = new B();
    // b.num = 5;
}
A::~A(){
    DEL_PTR(b);
}
void A::print(){
    b->print();
}
void A::B::print(){
    std::cout<<2;
}
int main(){
    A a;
    std::cout<<1<<std::endl;
    // a->b.print();
    // std::cout<<a.getb();
    a.print();
}
