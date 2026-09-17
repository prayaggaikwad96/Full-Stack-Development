#include <iostream>  

int main() {  
    int age;  
    float height;  
    std::string name;  
    std::cout << "Enter your name: ";  
    std::cin >> name;  
    std::cout << "Enter your age: ";  
    std::cin >> age;  
    std::cout << "Enter your height in meters: ";  
    std::cin >> height;  
    std::cout << "\n--- User Details ---\n";  
    std::cout << "Name: " << name << std::endl;  
    std::cout << "Age: " << age << " years" << std::endl;  
    std::cout << "Height: " << height << " meters" << std::endl;  
    return 0;  
}






















