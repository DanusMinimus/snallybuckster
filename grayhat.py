import sys, requests
import logging
from typing import List
from strongtyping.config import SEVERITY_LEVEL
from strongtyping.strong_typing import match_typing

const_mb_byte_size = 1048576
logging.basicConfig(format='[%(levelname)s]%(message)s', level=logging.INFO)

class ForbiddenAccess(Exception):
	pass

class Build:

	@match_typing(severity=SEVERITY_LEVEL.WARNING)
	def __init__(self, api_k: str = None):
		self.api_k = api_k
		self.url = 'https://buckets.grayhatwarfare.com/api/v1'

	@match_typing
	def Buckets(self, start_page = 0, stop_page=None, bucket_id=None, key_words: List[str] = [], full_path=0):
		bucket_query_url = self.url
		bucket_query_url += f'/bucket/{bucket_id}/files' if bucket_id else '/buckets'
		bucket_query_url += f'/{start_page}/{stop_page}' if stop_page else f'/{start_page}'
		bucket_query_url += f'?access_token={self.api_k}'
		if len(key_words) > 0 and bucket_id:
			bucket_query_url += f'&keywords='
			e = '%20' if len(key_words) > 1 else ''
			for k in key_words:
				n = key_words.index(k)
				if n > 0 and not k.startswith('-'):
					continue
				bucket_query_url += f'{k}{e}' if n < (len(key_words) -1) else f'{k}'
		elif len(key_words) > 0 and not bucket_id:
			bucket_query_url += f'&keywords={key_words[0]}'

		bucket_query_url += f'&full-path={full_path}' if full_path else f''
		return bucket_query_url

	@match_typing
	def Files(self, start_page = 0, stop_page=None, key_words: List[str] = [], ext: List[str] = []):
		file = f'{self.url}/files'
		if key_words and 0 < len(key_words) < 5:
			with open('exclude.txt', 'r') as negative:
				for trash in negative.read().split(','):
					if trash.startswith('-'):
						key_words += trash.split()
		if key_words and len(key_words) > 0:
			e = '%20' if len(key_words) > 1 else ''
			file += '/'
			for k in key_words:
				n = key_words.index(k)
				if n > 0 and not k.startswith('-'):
					continue
				file += f'{k}{e}' if n < (len(key_words) -1) else f'{k}'
		file += f'/%20' if len(key_words) < 1 else ''
		file += f'/{start_page}/{stop_page}' if stop_page else f'/{start_page}'
		file += f'?access_token={self.api_k}'
		if ext and len(ext) > 0:
			e = '%2C' if len(ext) > 1 else ''
			file += f'&extensions='
			for ex in ext:
				if ex.startswith('.'):
					ex = ex.replace('.', '')
				file += f'{ex}{e}'
		return file


class s3:
	@match_typing(severity=SEVERITY_LEVEL.WARNING)
	def __init__(self, query: str):
		self.query = query
		self.list = []
		self._json = ""
		self._total_files = 0

	@match_typing(severity=SEVERITY_LEVEL.WARNING)
	def perform_query(self):
		try:
			respose_object = requests.get(self.query, timeout=5)
			self._json = respose_object.json()
			self._total_files = self._json['results']
			return self._json
		except Exception as exp_error:
			logging.error("Exception! ", exp_error)
			sys.exit(0)

	def get_total_results(self):
		return self._total_files

	def get_json(self):
		return self._json

	def hunt(self):
		for data_dict in self._json['files']:
			return 0
			