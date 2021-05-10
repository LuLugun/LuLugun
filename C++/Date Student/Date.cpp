#include "Date.h"
#include <iostream>
using namespace std;

Date::Date()
{

}

Date::Date(int newmonth,int newday,int newyear)
{
	month = newmonth;
	day = newday;
	year = newyear;
}
int Date::getMonth()const
{
	return month;
}
int Date::getDay()const
{
	return day;
}
int Date::getYear()const
{
	return year;
}
void Date::setMonth(int newmonth)
{
	month = newmonth;
}
void Date::setDay(int newday)
{
	day = newday;
}
void Date::setYear(int newyear)
{
	year = newyear;
}
void Date::print()
{
	cout << month << "/" << day << "/" << year ;
}
