#include <iostream>
//#include <stdio>

class World
{
    public:
    World()
    {
        std::cout << "Hello World!" << std::endl;
    }
    
    ~World()
    {
        std::cout << "Good Bye!" << std::endl;
    }
};

World World();


int main()
{
  
  std::cout << "Hello CPP!";
  std::cout << "How are you?";
  return 0;
}
