
# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from main.models import *
from main.serializers import ArticleListSerializer, ArticlePostSerializer, ArticleDetailSerializer, \
    ArticleUpdateSerializer, ArticleCommentListSerializer, ReplyListSerializer, ArticleCommentPostSerializer, \
    ReplyPostSerializer, ArticleLikeSerializer


# TODO: search, filter, pagination
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = (AllowAny, )
    search_fields = ['title', ]
    ordering = ['created', ]

    def get_serializer_class(self):
        serializers_actions = {'create': ArticlePostSerializer,
                                'list': ArticleListSerializer,
                                'retrieve':  ArticleDetailSerializer,
                                'update': ArticleUpdateSerializer,
                                'partial_update': ArticleUpdateSerializer,
                               }

        return serializers_actions[self.action]


class ArticleCommentViewSet(ModelViewSet):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentListSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        serializers_actions = {'create': ArticleCommentPostSerializer,
                                'list': ArticleCommentListSerializer,
                                'retrieve':  ArticleCommentListSerializer,
                                'update': ArticleCommentListSerializer,
                                'partial_update': ArticleCommentListSerializer,
                               }

        return serializers_actions[self.action]


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplyListSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        serializers_actions = {'create': ReplyPostSerializer,
                                'list': ReplyListSerializer,
                                'retrieve':   ReplyListSerializer,
                                'update':  ReplyListSerializer,
                                'partial_update':  ReplyListSerializer,
                               }

        return serializers_actions[self.action]


class ArticleLikeViewSet(ModelViewSet):
    queryset = ArticleLike.objects.all()
    serializer_class = ArticleLikeSerializer
    permission_classes = (AllowAny,)




