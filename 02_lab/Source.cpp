#include<iostream>

int main()
{
	int n;
	std::cout << "n=";
	std::cin >> n;
	int sum=0;
	for (int i = 0; i <= n; i++)
	{
		sum += i;
	}
	std::cout << sum << std::endl;
	return 0;
}