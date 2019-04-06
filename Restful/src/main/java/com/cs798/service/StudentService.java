package com.cs798.service;

import com.cs798.dao.StudentRepository;
import com.cs798.entity.Student;
import com.cs798.vo.StudentVO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StudentService {
    @Autowired
    private StudentRepository studentRepo;

    public Student findStudentById(int id) {
        return studentRepo.findById(id);
    }

    public List<Student> findAllStudents() {
        return studentRepo.findAll();
    }

    public void addStudent(StudentVO studentVO) {
        Student student = new Student();
        student.setId(studentVO.getId());
        student.setName(studentVO.getName());
        studentRepo.save(student);
    }

    public void deleteStudent(int id){
        Student student = new Student();
        student.setId(id);
        studentRepo.delete(student);
    }
}
