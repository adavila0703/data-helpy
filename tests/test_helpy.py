from dbhelpy.dbhelpy import Helpy


class HelpyTest:
    db = Helpy('dummy.db')

    def test_get_all_data(self):
        data = self.db.get_all_data('cars')
        assert len(data) == 3
        assert type(data) == list

    def test_get_all_asc_by(self):
        data = self.db.get_all_asc_by('cars', 'id', 'color', 'red')
        assert len(data) == 2
        assert type(data) == list
        assert data[0][2] == 'red'

    def test_get_all_dec_by(self):
        data = self.db.get_all_dec_by('cars', 'id', 'color', 'red')
        assert len(data) == 2
        assert type(data) == list
        assert data[0][2] == 'red'

    def test_get_all_data_by(self):
        data = self.db.get_all_data_by('cars', 'color', 'red')
        assert len(data) == 2
        assert type(data) == list

    def test_get_all_column(self):
        data = self.db.get_all_column('cars', 'color')
        assert len(data) == 3
        assert type(data) == list
        assert data[0][0] == 'red'

    def test_get_column_by(self):
        data = self.db.get_column_by('cars', 'id', "color='red'")
        assert len(data) == 2
        assert type(data) == list
        assert data[0][0] == 1

    def test_get_calc_column(self):
        data = self.db.get_calc_column('cars', 'id')
        assert data == 6

    def test_get_cal_column_by(self):
        data = self.db.get_cal_column_by('cars', 'price', "color='red'")
        assert data == 75000
        assert type(data) == int

    def test_get_all_dec(self):
        data = self.db.get_all_dec('cars', 'price')
        assert type(data) == list
        assert len(data) == 3

    def test_get_all_asc(self):
        data = self.db.get_all_asc('cars', 'price')
        assert type(data) == list
        assert len(data) == 3

    def test_get_single_data(self):
        data = self.db.get_single_data('cars', 'id', 1)
        assert type(data) == str
        assert len(data) == 1

    def test_search_all_data(self):
        data = self.db.search_all_data('cars', 'red')
        assert type(data) == list
        assert len(data) == 1