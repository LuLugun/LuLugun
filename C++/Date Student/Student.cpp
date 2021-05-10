#include "Student.h"
#include "Date.h"
#include <iostream>
using namespace std;

Student::Student()
{

}
Student::Student(string newname, Date newbirthDay, int newscore)
{
	name = newname;
	birthDay = newbirthDay;
	score = newscore;
}
string Student::getName()const
{
	return name;
}
Date Student::getDate()const
{
	return birthDay;
}
int Student::getScore()const
{
	return score;
}
void Student::setName(string newname)
{
	name = newname;
}
void Student::setDate(Date newbirthDay)
{
	birthDay = newbirthDay;
}
void Student::setScore(int newscore)
{
	score = newscore;
}
void Student::print()
{
	cout << name  <<" ";
	birthDay.print();
	cout <<" "<< score << endl;
}