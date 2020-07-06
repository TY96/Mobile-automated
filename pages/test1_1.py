class pytry():
    def pytest_1(self,driver):
        self.driver = driver
        self.windows = "联想"
        self.computer= "苹果"
        return self.driver

p = pytry()
print(p.pytest_1("a"))
print(p.__dict__)
