class student:
      grade = 10
      name = "penguin"

      def introduction(self):
        print("Hi I am a student")

      def details(self):
            print("My name is", self.name)
            print("I Study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()
