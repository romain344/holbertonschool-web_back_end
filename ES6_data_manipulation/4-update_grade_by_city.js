function updateStudentGradeByCity(students, city, newGrade) {
    return students
        .filter((students) => students.location === city)
        .map((students) => {
            const student = { ...students };
            const gradeObj = student.grades.find((grade) => grade.course === 'Math');
            student.grade = gradeObj ? gradeObj.grade : 'N/A';
            if (student.grade !== 'N/A') {
                student.grade = newGrade;
            }
            return student;
        });
}