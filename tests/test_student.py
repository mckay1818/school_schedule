from school_schedule.student import Student

def test_initial_state():
    #Arrange
    name = "Claire"
    grade = "junior"
    classes = ["science", "art", "English", "Spanish"]
    
    #Act
    student1 = Student(name, grade, classes)

    #Assert
    assert student1.name == name
    assert student1.grade == grade
    assert len(student1.classes) == len(classes)
    assert "science" in student1.classes
    assert "art" in student1.classes
    assert "English" in student1.classes
    assert "Spanish" in student1.classes


def test_add_class():
    #Arrange
    english = "English"
    student1 = Student(
            "Samara", 
            "junior", 
            [ 
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition" 
            ]
        )
    #Act
    result = student1.add_class(english)
    
    #Assert
    assert english in student1.classes