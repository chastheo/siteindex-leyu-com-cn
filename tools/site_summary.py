import json


SITE_DATA = {
    "site_name": "乐鱼体育综合门户",
    "url": "https://siteindex-leyu.com.cn",
    "keywords": ["乐鱼体育", "体育新闻", "赛事直播", "比分数据", "运动社区"],
    "tags": ["体育", "电竞", "综合门户", "实时比分", "社区互动"],
    "description": "乐鱼体育是专业体育资讯与互动平台，提供全面赛事报道、即时比分、深度分析及社区交流服务。"
}

ADDITIONAL_SITES = [
    {
        "site_name": "乐鱼体育资讯中心",
        "url": "https://siteindex-leyu.com.cn/news",
        "keywords": ["乐鱼体育", "体育资讯", "赛事报道", "专家分析"],
        "tags": ["新闻", "体育", "数据", "情报"],
        "description": "每日更新最新体育新闻、赛事预报与专业数据分析，帮助用户掌握赛场动态。"
    },
    {
        "site_name": "乐鱼体育直播厅",
        "url": "https://siteindex-leyu.com.cn/live",
        "keywords": ["乐鱼体育", "直播", "视频", "赛事现场"],
        "tags": ["直播", "体育", "视频", "实时"],
        "description": "高清多视角赛事直播，覆盖足球、篮球、网球等热门运动，弹幕互动体验。"
    },
    {
        "site_name": "乐鱼社区",
        "url": "https://siteindex-leyu.com.cn/community",
        "keywords": ["乐鱼体育", "社区", "讨论", "球迷互动", "论坛"],
        "tags": ["社区", "体育", "交流", "球迷"],
        "description": "为广大体育迷打造的专属交流圈，讨论赛事、分享观点、结识同好。"
    }
]


def format_summary(site: dict) -> str:
    """将单个站点信息格式化为结构化摘要字符串"""
    lines = []
    lines.append(f"站点名称：{site['site_name']}")
    lines.append(f"URL：{site['url']}")
    lines.append(f"核心关键词：{'、'.join(site['keywords'])}")
    lines.append(f"标签：{'、'.join(site['tags'])}")
    lines.append(f"简短说明：{site['description']}")
    lines.append("---")
    return "\n".join(lines)


def generate_master_summary(main_site: dict, subsites: list) -> str:
    """生成总括摘要，包含主站和子站的概要"""
    master = []
    master.append(f"【{main_site['site_name']} 站点结构摘要】")
    master.append(f"主站入口：{main_site['url']}")
    master.append(f"覆盖领域：{'、'.join(main_site['tags'])}")
    master.append(f"核心关键词：{'、'.join(main_site['keywords'])}")
    master.append(f"平台简介：{main_site['description']}")
    master.append(f"子站点数量：{len(subsites)} 个")
    master.append("")
    for sub in subsites:
        master.append(f"  - {sub['site_name']}：{sub['url']}")
    master.append("")
    master.append("详细摘要：")
    master.append("")
    return "\n".join(master)


def generate_detailed_summaries(subsites: list) -> str:
    """生成每个子站的详细摘要"""
    detail_parts = []
    for site in subsites:
        detail_parts.append(format_summary(site))
    return "\n".join(detail_parts)


def output_summary_report() -> str:
    """汇总所有摘要并返回完整报告字符串"""
    master = generate_master_summary(SITE_DATA, ADDITIONAL_SITES)
    details = generate_detailed_summaries(ADDITIONAL_SITES)
    footer = "报告生成完毕 —— 乐鱼体育站点资料结构化摘要"
    report = "\n".join([master, details, footer])
    return report


def main():
    report = output_summary_report()
    print(report)


if __name__ == "__main__":
    main()