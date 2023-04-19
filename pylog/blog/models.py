from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('포스트 제목',max_length=100)
    content = models.TextField('포스트 내용')
    # 자신의 정보를 나타내는 함수
    def __str__(self):
        return self.title

class Comment(models.Model):
    # 다른 모델(테이블과) 1:N 연결을 구성해주는 ForeignKey 필드 사용
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')

    def __str__(self):
        return f'{self.post.title}의 댓글 (ID : {self.id})'