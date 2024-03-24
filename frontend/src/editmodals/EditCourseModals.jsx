import React, { useState } from "react";
import { CSSTransition } from "react-transition-group";
import axios from "axios";
import "./css/editcoursemodal.css";

const EditCourseModal = ({ isOpen, onClose, course }) => {
  const [courseName, setCourseName] = useState(course.course_name);


  const handleSubmit = async () => {
    try {
      await axios.put(`http://localhost:8000/api/courses/${course.course_number}/`, {
        course_name: courseName,

      });
      onClose(true); // Close the modal and refresh the data
    } catch (error) {
      console.error("Error updating course:", error);
    }
  };

  return (
    <CSSTransition in={isOpen} timeout={300} classNames="modal" unmountOnExit>
      <div className="modal" onClick={() => onClose(false)}>
        <div className="modal-content" onClick={(e) => e.stopPropagation()}>
          <h2>Edit Course</h2>
          <form onSubmit={handleSubmit}>
            <label>
              Course Name:
              <input type="text" value={courseName} onChange={(e) => setCourseName(e.target.value)} />
            </label>
            <div className="buttons">
              <button type="submit">Save</button>
              <button type="button" onClick={() => onClose(false)}>Cancel</button>
            </div>
          </form>
        </div>
      </div>
    </CSSTransition>
  );
};

export default EditCourseModal;
