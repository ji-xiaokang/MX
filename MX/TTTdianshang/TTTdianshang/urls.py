from apps.user_operation.views import UserFavViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView

__author__ = 'derek'

from django.urls import path,include,re_path
import xadmin
from django.views.static import serve
from TTTdianshang.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewSet, IndexCategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from app.views import SmsCodeViewset, UserViewset
from apps.user_operation.views import UserFavViewset, LeavingMessageViewset

router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet,basename='goods')
# 配置Category的url
router.register(r'categorys', CategoryViewSet, basename="categorys")
#发短信
router.register(r'code', SmsCodeViewset, basename="code")
#注册
router.register(r'users', UserViewset, basename="users")
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")
# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, basename="messages")
# 配置收货地址
router.register(r'address',AddressViewset , basename="address")
# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
# 配置订单的url
router.register(r'orders', OrderViewset, basename="orders")
# 配置首页轮播图的url
router.register(r'banners', BannerViewSet, basename="banners")
# 首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewSet, basename="indexgoods")




urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('ueditor/',include('DjangoUeditor.urls' )),
    #文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    #drf文档，title自定义
    path('docs',include_docs_urls(title='仙剑奇侠传')),
    #商品列表页
    re_path('^', include(router.urls)),
    # 登录验证token
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证接口
    path('login/', obtain_jwt_token),

    # 配置支付宝支付相关接口的url
    path('alipay/return/', AlipayView.as_view())


]
