#include <iostream>
#include "Student.h"
#include "Date.h"
using namespace std;

int main()
{
	Date birth1(6, 1, 1999);
	Date birth2(10, 8, 1997);
	Student student1("John", birth1, 90);
	Student student2("Marry", birth2, 80);
	string name1;
	int year1, month1, day1;
	cin >> name1 >> month1 >> day1 >>year1 ;
	Date birth3(month1, day1, year1);
	student1.setName(name1);
	student2.setDate(birth3);
	student1.print();
	student2.print();
	return 0;
}