# Types

Type: Article

## Data types in `MySQL`

In classical relational databases, values always come with a specific type. Understanding the differences between these types will later help us to optimize the database, query it, as well as to hold the data correctly.

It is important to understand that to a computer, information that looks the same to us, can be something completely different. For example, the string "1" is something different from the number 1.

## Where are types needed?

We will use data types mostly in 2 places:

- When creating new tables in databases,
- When using functions (which we will learn about later in the course).

In addition, it is useful to know the types of columns in a table so that you can filter it effectively.

### Example:

The table definition includes the definition of column types:

``` 
CREATE TABLE pet (
    name VARCHAR(20),
    owner VARCHAR(20),
    species VARCHAR(20),
    sex CHAR(1),
    birth DATE,
    death DATE
);
```

Here we use types to record characters and dates.

In this article we will learn about more advanced types than characters and dates.

## Numeric types

### Writing numeric values

Understanding the differences between the different types of numeric values is very important when using the database. Numeric types seem to be the simplest type, but there are many differences between them. The most important are:

- the range of the data being held - a poor choice of type can result in not being able to remember values and, for example, going out of range during aggregation,
- accuracy of the data held (number of decimal places) - the wrong number of decimal places can cause a loss of precision of our results.

### Example

Numeric types are used in scientific (usually floating-point), financial (often fixed-point) applications.

``` 
CREATE TABLE stock (
    ticker CHAR(3),
    day DATE,
    open DECIMAL(20,2),
    close DECIMAL(20,2),
    min DECIMAL(20,2),
    max DECIMAL(20,2),
    volume BIGINT
);
```

In the example, we have a table with stock market data including values with two decimal places describing the opening, closing, daily minimum and maximum. However, the number of transactions is a non-negative integer.

### Numeric types

| Type | Description |
| --- | --- |
| TINYINT | Very small integer (-128, 127) |
| SMALLINT | Small integer (-32768, 32767) |
| MEDIUMINT | Medium integer (-8M, 8M) |
| INT | Integer (-2 10^9, 2 10^9) |
| BIGINT | Big integer (-9 10^18, 9 10^18) |
| DECIMAL | Number with a fixed count of decimal places; good for financial values |
| FLOAT | Floating-point number (23 digits) |
| DOUBLE | Double-precision floating-point (24 to 53 digits) |
| BIT | Bit value from 1 to 64 bits |

### Detailed description of types

In many cases, we need to provide additional information (such as the range of numbers after the decimal point, which we mentioned earlier) to correctly specify the numeric type.

- `DECIMAL(M, D)` - where: M <= 65, D <= 30, M is the maximum count of total digits, D is for decimal digits.

### Example:

``` 
DECIMAL(5,2)
```

A good type to store values from -999.99 to 999.99 up the nearest hundredth. With such precision there will be no problems with approximations for addition.

- FLOAT(p) - 0 <= p <= 24 are treated as FLOAT, and 25 <= p <= 53 as a DOUBLE. Example:

``` 
FLOAT, FLOAT(12), FLOAT(5)
```

These types all correspond to the float type. Their precision spans 32 bits, which gives from a few up to a dozen decimal places. `MySQL` uses bit representation that depends on the machine on which the database is installed, so it is not possible to indicate the exact range. One can assume that it will probably be more or less 1 bit for the sign, 8 for the exponent and 23 for the fractional part.

- `DOUBLE(M, D)` - M maximum number of digits, D - number of decimal digits.

## String types

| Type | Description |
| --- | --- |
| CHAR | fixed length character(s) |
| VARCHAR | variable length characters |
| BINARY | fixed length binary string |
| VARBINARY | variable length binary string |
| TINYBLOB | Tiny binary object up to 255 B |
| BLOB | Small binary object up to 64 KB |
| MEDIUMBLOB | Medium binary object up to 16 MB |
| LONGBLOB | Huge binary object up to 4 GB |
| TINYTEXT | Very short text up to 255 characters |
| TEXT | Short text up to 65K characters - 35 standard pages |
| MEDIUMTEXT | Average text around 8-9K pages |
| LONGTEXT | Long text up to 2 million pages, 10K books on average |
| ENUM | One of possible elements |
| SET | Any unordered combination of elements |

## Date and time types

As with numeric types, there are many different ranges and precisions for determining time.

If we want to know the time to the precision of a year, over a thousand years we will need a different amount of memory than when specifying it to the precision of a second and maintaining a range of one century.

A typical manifestation of this issue is the so-called problem of the year 2038.

That is exactly when 2^31-1 seconds will have passed since January 1, 1970, when UNIX time began to be counted.

Another problem was the one related to the year 2000, where the clock zeroed in systems based on the representation of the year by two digits.

`MySQL` is a database capable of working with systems with different time-keeping conventions, and it is up to us which type we choose for our needs.

| Type | Description |
| --- | --- |
| DATE | CCYY-MM-DD format date |
| TIME | hh:mm:ss format time |
| DATETIME | CCYY-MM-DD hh:mm:ss format date and time from year 1000 to 9999 |
| TIMESTAMP | CCYY-MM-DD hh:mm:ss format date and time from 1970 to 2038 |
| YEAR | Year written as CCYY or YY |

### Example

Dates do not contain time zone information. We can set the time zone with the command:

``` 
SET time_zone ='+03:00';
```

We get automatic logging of creation and update time with:

``` 
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```
