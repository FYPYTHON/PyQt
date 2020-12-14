#include<iostream>
#define DEL_PTR(p) if(p) delete p;p=NULL;
class NodeValue{
public:
    static NodeValue* create();
    static void destroy(NodeValue* num);
    //static void destroy();
    int getValue();
    int* getNum();
private:
    NodeValue();
    ~NodeValue();
    int* num;
    class Impl;
    Impl* _impl;

};
class NodeValue::Impl
{
public:
    int getValue();
private:
    int _val;
};
int NodeValue::Impl::getValue(){
    _val = 5;
    return _val;
}

NodeValue* NodeValue::create(){
    return new NodeValue();
}

void NodeValue::destroy(NodeValue* num){
    std::cout<<"destroy~NodeValue();"<<num<<std::endl;
    if(num){
        delete num;
        num = NULL;
    }
}
NodeValue::NodeValue(){
    std::cout<<"¹¹ÔìNodeValue();"<<std::endl;
    num = new int(10);
    std::cout<<"num:"<<num<<"="<<*num<<std::endl;
    _impl = new Impl();

}
NodeValue::~NodeValue(){
    std::cout<<"Îö¹¹~NodeValue();"<<std::endl;
    if(num){
        delete num;
        num = NULL;
    }
    DEL_PTR(_impl);
}
int NodeValue::getValue(){
    std::cout<<"getValue():"<<num<<std::endl;
    //int n = _impl->getValue();
    //num = &_impl->getValue();
    return _impl->getValue();;
}
int* NodeValue::getNum(){
    return num;
}
void test(){
    int ii = 5;
    int* p = &ii;
    std::cout<<"int:"<<ii<<","<<p<<","<<*p<<std::endl;
}
int main(){
    NodeValue *p = NodeValue::create();

    int value = p->getValue();
    std::cout<<"p-> " <<p<<","<<value<<std::endl;
    std::cout<<"value:"<<value<<std::endl;
    std::cout<<"num:"<<p->getNum()<<","<<*(p->getNum())<<std::endl;
    p->destroy(p);
    std::cout<<"test..."<<std::endl;
    test();
    int n_len = 9;
    std::cout<<"n_len:"<<--n_len<<std::endl;
    char* s = 0;
    std::cout<<"char *s:"<<s<<std::endl;
    return 0;
}
