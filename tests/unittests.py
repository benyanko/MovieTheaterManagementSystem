import unittest
import requests
from concurrent.futures import ThreadPoolExecutor


class TestRequests(unittest.TestCase):
    def test_get_available_chairs(self):
        res = requests.get('http://127.0.0.1:5000/chair')
        print({'response': res.json()})
        self.assertEqual(res.status_code, 200)

    def test_get_orders(self):
        res = requests.get('http://127.0.0.1:5000/order')
        print({'response': res.json()})
        self.assertEqual(res.status_code, 200)

    def test_add_chair(self):
        row = '2'
        chair_num = '100'

        res = requests.post('http://127.0.0.1:5000/chair', data={'row': row, 'chair_num': chair_num})
        print({'response': res.json()})
        self.assertEqual(res.status_code, 201)

    def test_order_chair(self):
        _id = '8'

        res = requests.post('http://127.0.0.1:5000/order/{0}'.format(_id))
        print({'response': res.json()})
        self.assertEqual(res.status_code, 200)

    def test_pay_order(self):
        _id = '8',
        confirmation_id = 'confirm'

        res = requests.post('http://127.0.0.1:5000/order/{0}/{1}'.format(_id, confirmation_id))
        print({'response': res.json()})
        self.assertEqual(res.status_code, 200)

    def test_cancel_order(self):
        _id = '8',
        confirmation_id = 'confirm'

        res = requests.put('http://127.0.0.1:5000/order/{0}/{1}'.format(_id, confirmation_id))
        print({'response': res.json()})
        self.assertEqual(res.status_code, 200)

    def test_async_order_chair(self):
        def test(_id):
            return requests.post('http://127.0.0.1:5000/order/{0}'.format(_id))

        id_list = [num for num in range(1,201)]*20

        counter = 0
        current = -1
        id_list.sort()
        for id in id_list:
            if id != current:
                counter += 1
                current = id


        with ThreadPoolExecutor(max_workers=12) as pool:
            response_list = list(pool.map(test, id_list))
        res_counter = 0
        for response in response_list:
            if response.ok:
                res_counter += 1
            print(response.json())
        self.assertEqual(res_counter, counter)

    def test_async_get_req(self):
        def test(url):
            return requests.get(url)

        counter = 100
        url_list = ['http://127.0.0.1:5000/chair']*counter

        with ThreadPoolExecutor(max_workers=10) as pool:
            response_list = list(pool.map(test, url_list))
        res_counter = 0
        for response in response_list:
            if response.ok:
                res_counter += 1
            print(response.json())
        self.assertEqual(res_counter, counter)


if __name__ == '__main__':
    unittest.main()
