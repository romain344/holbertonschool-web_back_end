export default function getStudentsByLocation(city) {
    if (!Array.isArray(getListStudentIdss))
        return [];
    return getListStudentIdss().filter((student) => student.location === city);
}