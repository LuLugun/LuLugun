#ifndef DATE_H
#define DATE_H
#include <iostream>
using namespace std;
class Date
{
public:
	Date();
	Date(int, int, int);
	void setMonth(int);
	void setDay(int);
	void setYear(int);
	int getMonth()const;
	int getDay()const;
	int getYear()const;
	void print();
private:
	int month, day, year;

};
#endif
