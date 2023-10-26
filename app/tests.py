from django.test import SimpleTestCase


class TestNearHundredView(SimpleTestCase):
    def test_93_near_100(self):
        response = self.client.get("/warmup-1/near-hundred/93/")
        self.assertContains(response, "True")

    def test_90_near_100(self):
        response = self.client.get("/warmup-1/near-hundred/90/")
        self.assertContains(response, "True")

    def test_89_near_100(self):
        response = self.client.get("/warmup-1/near-hundred/89/")
        self.assertContains(response, "False")


class TestStringSplosionView(SimpleTestCase):
    def test_Code_splosion(self):
        response = self.client.get("/warmup-2/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_abc_splosion(self):
        response = self.client.get("/warmup-2/string-splosion/abc/")
        self.assertContains(response, "aababc")

    def test_ab_splosion(self):
        response = self.client.get("/warmup-2/string-splosion/ab/")
        self.assertContains(response, "aab")


class TestCatDogView(SimpleTestCase):
    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/catdog/")
        self.assertContains(response, "True")

    def test_catcat(self):
        response = self.client.get("/string-2/cat-dog/catcat/")
        self.assertContains(response, "False")

    def test_1cat1cadodog(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog/")
        self.assertContains(response, "True")


class TestLoneSumView(SimpleTestCase):
    def test_1_2_3_lone_sum(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3/")
        self.assertContains(response, "6")

    def test_3_2_3_lone_sum(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3/")
        self.assertContains(response, "2")

    def test_3_3_3_lone_sum(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3/")
        self.assertContains(response, "0")
