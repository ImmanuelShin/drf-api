from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import DRF 

class DRFTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_drf = DRF.objects.create(
            name="Digital Rangefinder",
            owner=testuser1,
            description="A modern optical device equipped with electronic sensors and imaging technology that measures the distance between the device and a target, commonly used in photography, surveying, and sports such as golf.",
        )
        test_drf.save()

    def test_drf_model(self):
        drf_instance = DRF.objects.get(id=1)
        actual_owner = str(drf_instance.owner)
        actual_name = str(drf_instance.name)
        actual_description = str(drf_instance.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Digital Rangefinder")
        self.assertEqual(
            actual_description, "A modern optical device equipped with electronic sensors and imaging technology that measures the distance between the device and a target, commonly used in photography, surveying, and sports such as golf."
        )

    def test_get_drf_list(self):
        url = reverse("drf_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drfs = response.data
        self.assertEqual(len(drfs), 1)
        self.assertEqual(drfs[0]["name"], "Digital Rangefinder")

    def test_get_drf_by_id(self):
        url = reverse("drf_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf_instance = response.data
        self.assertEqual(drf_instance["name"], "Digital Rangefinder")

    def test_create_drf(self):
        url = reverse("drf_list")
        data = {"owner": 1, "name": "Dual Role Fighter", "description": "A versatile military aircraft designed to perform both air-to-air combat and ground-attack missions, capable of engaging enemy aircraft as well as carrying out strikes against ground targets."}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        drfs = DRF.objects.all()
        self.assertEqual(len(drfs), 2)
        self.assertEqual(DRF.objects.get(id=2).name, "Dual Role Fighter")

    def test_update_drf(self):
        url = reverse("drf_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Digital Rangefinder",
            "description": "A modern optical device equipped with electronic sensors and imaging technology that measures the distance between the device and a target, commonly used in photography, surveying, and sports such as golf.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf_instance = DRF.objects.get(id=1)
        self.assertEqual(drf_instance.name, data["name"])
        self.assertEqual(drf_instance.owner.id, data["owner"])
        self.assertEqual(drf_instance.description, data["description"])

    def test_delete_drf(self):
        url = reverse("drf_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        drfs = DRF.objects.all()
        self.assertEqual(len(drfs), 0)
