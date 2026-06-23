# Adding new teacher

Type: Exercise

Write a following query:

1. Try to add a new teacher to the database with the following data:
  
  - `teacher_id` - 2
  - `name` - John Koval
  - `pay` - 1300
    
    Has adding the teacher worked? If not, what error the database returned?
2. Add the teacher from the previous point, specifying only his name and salary. Do not give the primary key (`teacher_id` field),
3. Load all teachers. What primary key has been assigned to Jan Kowalski?
4. Try adding a new teacher by giving all fields (together with the primary key – `teacher_id` field). But this time as the `teacher_id` give the value that does not yet exist in the table (e.g. greater by one than the last value in the filed).
