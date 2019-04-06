package com.cs798.dao;

import com.cs798.entity.Student;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface StudentRepository extends CrudRepository<Student,Integer> {
    Student findById(int id);
    List<Student> findAll();
}
