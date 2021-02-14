// Допишите программу, которая печатает абсолютное значение числа, введённого 
// с клавиатуры пользователем.

#include <iostream>

int main() {
    double absolute_value;
    std::cout << "x=";
    std::cin >> absolute_value;

    if (absolute_value >= 0)
    {
        std::cout << absolute_value << std::endl;
    }
    if (absolute_value < 0)
    {
        absolute_value = -absolute_value;
        std::cout << absolute_value << std::endl;
    }
    //std::cout << absolute_value << std::endl;
}
