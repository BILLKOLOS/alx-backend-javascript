
export default class HolbertonClass {
	rt default function getStudentsByLocation(students, city) {
		  return students.filter((student) => student.location === city);
	}
