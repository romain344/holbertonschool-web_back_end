export default function getListStudentIds() {
    if (!Array.isArray(getListStudents))
        return [];
    return list.map((s) => s.id);
}