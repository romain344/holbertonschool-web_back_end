function getListStudentIds() {
    if (!Array.isArray(getListStudents))
        return [];
    return getListStudents().map((student) => student.id);
}