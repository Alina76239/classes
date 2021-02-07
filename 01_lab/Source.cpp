#include<iostream>

int main()
{
	int a;
	std::cout << "a=";
	std::cin >> a;
	do
	{
		int d = a % 10;
		std::cout << d << "";
		a /= 10;
	} while (a);
	
	return 0;
}