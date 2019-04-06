package com.cs798.controller;

import com.cs798.entity.Student;
import com.cs798.service.StudentService;
import com.cs798.vo.StudentVO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/api")
public class StudentController {
    @Autowired
    private StudentService service;

    @GetMapping(value = "/student")
    public List<Student> getAllStudents() {
        return service.findAllStudents();
    }

    @GetMapping(value = "/student/{studentId}")
    public Student getStudent(@PathVariable("studentId") int userId) {
        return service.findStudentById(userId);
    }

    @PostMapping(value="/student")
    public String addStudent(@RequestBody StudentVO studentVO){
        service.addStudent(studentVO);
        return "success";
    }

    @DeleteMapping(value = "/student/{studentId}")
    public String deleteStudent(@PathVariable("studentId") int userId){
        service.deleteStudent(userId);
        return "success";
    }
}
