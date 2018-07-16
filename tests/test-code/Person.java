/**
 * A class that represents a Person
 */

public class Person {

    private String firstName;
    private String lastName;
    private int age;

    /**
     * Constructs a Person object with the given parameters
     * @param firstName First name of person
     * @param lastName Last name of person
     * @param age Age of person
     */

    public Person(String firstName, String lastName, int age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", age=" + age +
                '}';
    }

    public static void main(String[] args) {
        Person person = new Person("John", "Smith", 32);

        System.out.println(person);
    }

}