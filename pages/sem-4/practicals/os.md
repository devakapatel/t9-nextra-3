# Operating Systems

## Practical 1-2 : 50 Linux commands

[50 Linux Commands List with Examples - javatpoint](https://www.javatpoint.com/linux-commands)

## Practical 3

AIM: Write a shell script to generate mark-sheet of a student. Take 3 subjects, calculate and display total marks, percentage and Class obtained by the student.

```bash
echo "Student Marksheet"
echo "*****************"
echo "Enter Operating System Marks:"
read os
echo "Enter C++ Marks:"
read cpp
echo "Enter Java Marks:"
read java
echo "*****************"
total=`expr $os + $cpp + $java`
echo "Total Marks:" $total
percentage=`expr $total / 3`
echo "Percentage:" $percentage %
if [ $percentage -ge 60 ]
then
  echo "Class: First Class Distinction"
elif [ $percentage -ge 50 ]
then
  echo "Class: First class"
elif [ $percentage -ge 40 ]
then
  echo "Class: Second class"
else
  echo "Class: Fail"
fi
```

## Practical 4

AIM: Write a shell script to find factorial of given number n.

```bash
fact=1
read -p "Enter a number to find its factorial: " n

if [ $n -le 0 ]; then
  echo "Invalid number"
  exit 1
fi

a=$n
while [ $a -ge 1 ]; do
  fact=`expr $fact \* $a`
  a=`expr $a - 1`
done

echo "Factorial of $n is $fact"
```

## Practical 5

AIM: Write a shell script which will accept a number b and display first n prime numbers as output.

```bash
read -p "Enter the value of n (or range): " n
echo "The prime numbers are: "
m=2
while [ $m -le $n ]
do
  i=2
  flag=0
  while [ $i -le `expr $m / 2` ]
  do
    if [ `expr $m % $i` -eq 0 ]
    then
      flag=1
      break
    fi
    i=`expr $i + 1`
  done
  if [ $flag -eq 0 ]
  then
    echo $m
  fi
  m=`expr $m + 1`
done
```

## Practical 6

AIM: Write a shell script which will generate first n Fibonacci numbers like: 1, 1, 2, 3, 5, 13,...

```bash
read -p "Enter the value of n (number): " n
x=0
y=1
i=2
echo "Fibonacci Series up to $n terms is : "
echo "$x"
echo "$y"
while [ $i -lt $n ]
do
  i=`expr $i + 1`
  z=`expr $x + $y`
  echo "$z"
  x=$y
  y=$z
done
```

## Practical 7.1

Aim:

1. Display calendar of current month
2. Display today’s date and time
3. Display user names those are currently logged in the system
4. Display your name at given x, y position.
5. Display your terminal number

```bash
echo "Select Anyone Option"
echo "**************************************************"
echo "1) Display Calendar of the current month"
echo "2) Display Today's Date and Time"
echo "3) Display Username of users currently logged in"
echo "4) Display your name at a given x,y position"
echo "5) Display your terminal Number"
echo "6) Exit"
echo "Enter your choice:"
read ch

case $ch in
1) cal ;;
2) date ;;
3) who ;;
4) row=$(tput lines)
   col=$(tput cols)
   echo "Terminal Window has Rows=$row Cols=$col"
   echo "Enter desired X,Y position"
   echo "X position="
   read x
   echo "Y position="
   read y
   echo "Enter the name"
   read name
   tput cup $x $y
   echo "$name" ;;
5) tty ;;
6) echo "Exit" ;;
*) echo "Enter a valid choice" ;;
esac
```

## Practical 7.2

AIM: Write a shell script to read n numbers as command arguments and sort them in descending order.

```bash
read -p "Enter the number of values you want to sort: " n

for ((i=0; i<$n; i++))
do
    read -p "Enter value of arr[$i]: " arr[$i]
done

for ((i=0; i<$n; i++))
do
    for ((j=0; j<$n-i-1; j++))
    do
        if [ ${arr[j]} -lt ${arr[$((j+1))]} ]
        then
            # Swapping
            temp=${arr[j]}
            arr[$j]=${arr[$((j+1))]}
            arr[$((j+1))]=$temp
        fi
    done
done

echo "Numbers sorted in descending order:"
echo ${arr[*]}
```

## Practical 8.1

AIM: Write a shell script to check entered string is palindrome or not.

```bash
echo "Input your string without space"
read vstr
rvstr=""
for ((i=${#vstr}-1; i>=0; i--))
do
  rvstr="$rvstr${vstr:$i:1}"
done

echo "Input string was: $vstr"
echo "After Reversing String Is: $rvstr"

if [ "$vstr" = "$rvstr" ]
then
  echo "String Is Palindrome."
else
  echo "String Is Not Palindrome."
fi
```

## Practical 8.2

AIM: Write a shell script to validate the entered date. (eg. Date format is : dd-mm-yyyy).

```bash
# store day, month and year
dd=0
mm=0
yy=0
# store number of days in a month
days=0
# get day, month and year
echo -n "Enter day (dd) : "
read dd
echo -n "Enter month (mm) : "
read mm
echo -n "Enter year (yyyy) : "
read yy
# if month is negative (<0) or greater than 12
# then it is invalid month
if [ $mm -le 0 -o $mm -gt 12 ]; then
    echo "$mm is an invalid month."
    exit 1
fi
# Find out number of days in given month
case $mm in
    1) days=31 ;;
    2) days=28 ;;
    3) days=31 ;;
    4) days=30 ;;
    5) days=31 ;;
    6) days=30 ;;
    7) days=31 ;;
    8) days=31 ;;
    9) days=30 ;;
    10) days=31 ;;
    11) days=30 ;;
    12) days=31 ;;
    *) days=-1 ;;
esac
# find out if it is a leap year or not
if [ $mm -eq 2 ]; then # if it is feb month then only check of leap year
    if [ $((yy % 4)) -ne 0 ]; then
        : # not a leap year : means do nothing and use old value of days
    elif [ $((yy % 400)) -eq 0 ]; then
        # yes, it's a leap year
        days=29
    elif [ $((yy % 100)) -eq 0 ]; then
        : # not a leap year do nothing and use old value of days
    else
        # it is a leap year
        days=29
    fi
fi
# if day is negative (<0) and if day is more than
# that month's days then day is invalid
if [ $dd -le 0 -o $dd -gt $days ]; then
    echo "$dd day is invalid"
    exit 3
fi
# if no error that means date dd/mm/yyyy is a valid one
echo "$dd/$mm/$yy is a valid date"
```

## Practical 8.3

AIM: Write an awk program using function, which convert each word in a given text into capital.

```bash
echo "Enter the String"
a=$(awk 'BEGIN{ getline str; print toupper(str); }')
echo $a
```

## Practical 9.1

AIM: The distance between two cities (in km.) is input through the keyboard. Write a shell script to convert and print distance in meters, feet, inches and centimeters

_This program may not run in many bash terminals as command `bc` is generally not installed in most Linux systems._

```bash
echo -n "Enter distance in km : "
read km
m=`echo $km * 1000 |bc`
cm=`echo $m * 100 |bc`
ft=`echo $cm / 30 |bc`
in=`echo $cm / 2.5 |bc`
echo "Distance in meters : $m"
echo "Distance in feets : $ft"
echo "Distance in inches : $in"
echo "Distance in centimeters : $cm"
```

## Practical 9.2

AIM: Write a shell script to input two no’s from the user and perform addition, subtraction, multiplication, division and modulation.

```bash
#!/bin/sh
a=10
b=20
val=`expr $a + $b`
echo "a + b : $val"
val=`expr $a - $b`
echo "a - b : $val"
val=`expr $a \* $b`
echo "a * b : $val"
val=`expr $b / $a`
echo "b / a : $val"
val=`expr $b % $a`
echo "b % a : $val"
if [ $a -eq $b ]
then
echo "a is equal to b"
fi
if [ $a -ne $b ]
then
echo "a is not equal to b"
fi
```

## Practical 9.3

AIM: Any integer is input through the keyboard. Write a shell script to find out whether it is an odd number or even number.

```bash
echo "---- EVEN OR ODD IN SHELL SCRIPT -----"
echo -n "Enter a number: "
read n
echo -n "RESULT: "
if [ `expr $n % 2` -eq 0 ]; then
    echo "$n is even"
else
    echo "$n is odd"
fi
```

## Practical 9.4

AIM: Write a shell script which receives any year form the keyboard and determines whether the year is a leap year or not. If no argument is supplied the current year should be assumed.

```bash
echo "Enter Year"
read yr

if [ `expr $yr % 4` -eq 0 -a \( `expr $yr % 400` -eq 0 -o `expr $yr % 100` -ne 0 \) ]; then
    echo "Entered year is a leap year"
else
    echo "Entered year is not a leap year"
fi
```

## Practical 10.1

AIM: Write a shell script to print the series 1, 3, 5, 7, 9, ......., 300.

```bash
for num in {1..300..2}
do
echo "Number: $num"
done
```

## Practical 10.2

AIM: Write a program to print all prime no’s from 1 to 300.

```bash
#!/bin/bash
for num in {2..300}
do
is_prime=true
for (( i=2; i<num; i++ ))
do
if [ $(($num%$i)) -eq 0 ]
then
is_prime=false
break
fi
done
if $is_prime
then
echo $num
fi
done
```
