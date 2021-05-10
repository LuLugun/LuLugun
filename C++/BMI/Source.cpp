#include <iostream>
#include<iomanip>
#include "BMI.h"
using namespace std;

int main()
{
	string name;
	double w1;
	double h1;
	cin >> name >> w1 >> h1;
	BMI bmi(w1, h1);
	cout << name << fixed << setprecision(2) << bmi.getBMI();
	return 0;
}