from django.urls import path
from . import apis

urlpatterns = [
    # User Public Profile pages API
    path(
        "profile/<str:username>/home/",
        apis.HomeProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/about-me/",
        apis.AboutMeProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/contact-me/",
        apis.ContactMeProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/contact-me/send/",
        apis.ContactMessageSend.as_view(),
    ),
    path(
        "profile/<str:username>/resume/",
        apis.ResumeProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/portfolio/",
        apis.PortfolioProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/portfolio/<str:slug>/",
        apis.PortfolioDetailProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/blog/",
        apis.BlogProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/blog/post/<str:slug>/",
        apis.BlogDetailProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/blog/search/<str:query>/",
        apis.BlogSearchPage.as_view(),
    ),
    path(
        "profile/<str:username>/blog/category/<str:category_name>/",
        apis.BlogCategoryPage.as_view(),
    ),
    path(
        "profile/<str:username>/appointments/",
        apis.AppointmentProfilePage.as_view(),
    ),
    path(
        "profile/<str:username>/appointments/request/",
        apis.RequestedAppointmentForm.as_view(),
    ),
    # User Dashboard APIs
    path(
        "dashboard/statistics/",
        apis.Staticstics.as_view(),
    ),
    path(
        "dashboard/edit-profile/",
        apis.EditProfile.as_view(),
    ),
    path(
        "dashboard/website-settings/",
        apis.WebsiteSettings.as_view(),
    ),
    path(
        "dashboard/general-settings/",
        apis.GeneralSettings.as_view(),
    ),
    path(
        "dashboard/seo-settings/",
        apis.SEOSettings.as_view(),
    ),
    path(
        "dashboard/about-me-settings/",
        apis.AboutMeSettings.as_view(),
    ),
    path(
        "dashboard/contact-information-settings/",
        apis.ContactInformationSettings.as_view(),
    ),
    path(
        "dashboard/statistics-settings/",
        apis.StatisticsSettings.as_view(),
    ),
    path(
        "dashboard/social-links-settings/",
        apis.SocialLinksSettings.as_view(),
    ),
    path(
        "dashboard/services/",
        apis.ServiceList.as_view(),
    ),
    path(
        "dashboard/service/<int:id>/",
        apis.ServiceDetail.as_view(),
    ),
    path(
        "dashboard/pricing-plans/",
        apis.PricingPlansList.as_view(),
    ),
    path(
        "dashboard/pricing-plan/<int:id>/",
        apis.PricingPlansDetail.as_view(),
    ),
    path(
        "dashboard/educations/",
        apis.EducationList.as_view(),
    ),
    path(
        "dashboard/education/<int:id>/",
        apis.EducationDetail.as_view(),
    ),
    path(
        "dashboard/experiences/",
        apis.ExperienceList.as_view(),
    ),
    path(
        "dashboard/experience/<int:id>/",
        apis.ExperienceDetail.as_view(),
    ),
    path(
        "dashboard/project-categories/",
        apis.ProjectCategoryList.as_view(),
    ),
    path(
        "dashboard/project-category/<int:id>/",
        apis.ProjectCategoryDetail.as_view(),
    ),
    path(
        "dashboard/projects/",
        apis.ProjectList.as_view(),
    ),
    path(
        "dashboard/project/<int:id>/",
        apis.ProjectDetail.as_view(),
    ),
    path(
        "dashboard/blog-categories/",
        apis.BlogCategoryList.as_view(),
    ),
    path(
        "dashboard/blog-category/<int:id>/",
        apis.BlogCategoryDetail.as_view(),
    ),
    path(
        "dashboard/blogs/",
        apis.BlogList.as_view(),
    ),
    path(
        "dashboard/blog/<int:id>/",
        apis.BlogDetail.as_view(),
    ),
    path(
        "dashboard/skill-categories/",
        apis.SkillCategoryList.as_view(),
    ),
    path(
        "dashboard/skill-category/<int:id>/",
        apis.SkillCategoryDetail.as_view(),
    ),
    path(
        "dashboard/skills/",
        apis.SkillList.as_view(),
    ),
    path(
        "dashboard/skill/<int:id>/",
        apis.SkillDetail.as_view(),
    ),
]
