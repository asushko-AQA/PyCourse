from playwright.sync_api import Page, expect

from .pages.course_map_page import CourseMapPage


def _unlock_lesson_4_1(page: Page) -> None:
    """Lesson 4.1 requires course-3/lesson-3-3 in the progress store."""
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )


def test_course3_bonus_block_visible_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    expect(
        course.page.get_by_role(
            "heading", name="Bonus ★ Star Projects (optional)"
        )
    ).to_be_visible()
    course.open_lesson_node("course-3", "lesson-4-1")
    course.expect_url_path("/en/course-3/block-4/lesson-4-1")
    expect(
        course.page.get_by_role("heading", name="Gravity & Flap")
    ).to_be_visible()


def test_course3_bonus_block_visible_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    expect(
        course.page.get_by_role(
            "heading", name="Бонус ★ Проекты (опционально)"
        )
    ).to_be_visible()
    course.open_lesson_node("course-3", "lesson-4-1")
    course.expect_url_path("/ru/course-3/block-4/lesson-4-1")
    expect(
        course.page.get_by_role("heading", name="Гравитация и взмах")
    ).to_be_visible()


def test_course3_home_lesson_count_includes_bonus(page, base_url: str) -> None:
    course = CourseMapPage(page, base_url)
    course.goto("/en")
    card = course.page.get_by_test_id("course-card-course-3")
    expect(card).to_contain_text("57 lessons")


def test_course3_prism_dash_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-3"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-4-4")
    course.expect_url_path("/en/course-3/block-4/lesson-4-4")
    expect(course.page.get_by_role("heading", name="Auto Scroll & Runner")).to_be_visible()


def test_course3_prism_dash_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-3"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-4-4")
    course.expect_url_path("/ru/course-3/block-4/lesson-4-4")
    expect(
        course.page.get_by_role("heading", name="Автопрокрутка и бегун")
    ).to_be_visible()


def test_course3_shard_stack_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-6"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-4-7")
    course.expect_url_path("/en/course-3/block-4/lesson-4-7")
    expect(
        course.page.get_by_role("heading", name="Grid & Cells")
    ).to_be_visible()


def test_course3_shard_stack_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-6"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-4-7")
    course.expect_url_path("/ru/course-3/block-4/lesson-4-7")
    expect(
        course.page.get_by_role("heading", name="Сетка и клетки")
    ).to_be_visible()


def test_course3_glyph_grove_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-9"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-4-10")
    course.expect_url_path("/en/course-3/block-4/lesson-4-10")
    expect(
        course.page.get_by_role("heading", name="Tiles & Layout")
    ).to_be_visible()


def test_course3_glow_worm_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-12"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    expect(
        course.page.get_by_role(
            "heading", name="Bonus ★ Star Projects II (optional)"
        )
    ).to_be_visible()
    course.open_lesson_node("course-3", "lesson-5-1")
    course.expect_url_path("/en/course-3/block-5/lesson-5-1")
    expect(
        course.page.get_by_role("heading", name="Grid & Segments")
    ).to_be_visible()


def test_course3_glow_worm_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-12"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    expect(
        course.page.get_by_role(
            "heading", name="Бонус ★ Проекты II (опционально)"
        )
    ).to_be_visible()
    course.open_lesson_node("course-3", "lesson-5-1")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-1")
    expect(
        course.page.get_by_role("heading", name="Сетка и сегменты")
    ).to_be_visible()


def test_course3_bounce_forge_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-3"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-4")
    course.expect_url_path("/en/course-3/block-5/lesson-5-4")
    expect(
        course.page.get_by_role("heading", name="Ball & Wall Bounces")
    ).to_be_visible()


def test_course3_bounce_forge_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-3"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-4")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-4")
    expect(
        course.page.get_by_role("heading", name="Мяч и отскоки от стен")
    ).to_be_visible()


def test_course3_orbit_guard_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-7"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-8")
    course.expect_url_path("/en/course-3/block-5/lesson-5-8")
    expect(
        course.page.get_by_role("heading", name="Patrol Ship & Blasters")
    ).to_be_visible()


def test_course3_orbit_guard_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-7"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-8")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-8")
    expect(
        course.page.get_by_role("heading", name="Патрульный корабль и выстрелы")
    ).to_be_visible()


def test_course3_mine_whisper_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-11"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-12")
    course.expect_url_path("/en/course-3/block-5/lesson-5-12")
    expect(
        course.page.get_by_role("heading", name="Crystal Grid & Clicks")
    ).to_be_visible()


def test_course3_mine_whisper_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-11"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-12")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-12")
    expect(
        course.page.get_by_role("heading", name="Сетка кристаллов и клики")
    ).to_be_visible()


def test_course3_merge_magic_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-15"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-16")
    course.expect_url_path("/en/course-3/block-5/lesson-5-16")
    expect(
        course.page.get_by_role("heading", name="Rune Lattice & Spawn")
    ).to_be_visible()


def test_course3_merge_magic_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-15"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-16")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-16")
    expect(
        course.page.get_by_role("heading", name="Руническая решётка и появление")
    ).to_be_visible()


def test_course3_twin_cards_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-18"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-19")
    course.expect_url_path("/en/course-3/block-5/lesson-5-19")
    expect(
        course.page.get_by_role("heading", name="Symbol Deck & Grid")
    ).to_be_visible()


def test_course3_twin_cards_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-18"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-19")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-19")
    expect(
        course.page.get_by_role("heading", name="Колода символов и сетка")
    ).to_be_visible()


def test_course3_tic_tac_bot_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-21"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-22")
    course.expect_url_path("/en/course-3/block-5/lesson-5-22")
    expect(
        course.page.get_by_role("heading", name="Grid & Hot-Seat Turns")
    ).to_be_visible()


def test_course3_tic_tac_bot_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-21"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-22")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-22")
    expect(
        course.page.get_by_role("heading", name="Сетка и ходы по очереди")
    ).to_be_visible()


def test_course3_leap_lands_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-24"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-25")
    course.expect_url_path("/en/course-3/block-5/lesson-5-25")
    expect(
        course.page.get_by_role("heading", name="Player & Jump")
    ).to_be_visible()


def test_course3_leap_lands_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-24"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-25")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-25")
    expect(
        course.page.get_by_role("heading", name="Игрок и прыжок")
    ).to_be_visible()


def test_course3_night_swarm_lesson_en(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-29"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-3")
    course.open_lesson_node("course-3", "lesson-5-30")
    course.expect_url_path("/en/course-3/block-5/lesson-5-30")
    expect(
        course.page.get_by_role("heading", name="Lantern Keeper Move")
    ).to_be_visible()


def test_course3_night_swarm_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-5-29"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-5-30")
    course.expect_url_path("/ru/course-3/block-5/lesson-5-30")
    expect(
        course.page.get_by_role("heading", name="Ходьба со светильником")
    ).to_be_visible()


def test_course3_glyph_grove_lesson_ru(page, base_url: str) -> None:
    _unlock_lesson_4_1(page)
    page.add_init_script(
        """
        localStorage.setItem(
          "pyquest-progress",
          JSON.stringify({
            state: {
              xp: 0,
              completedLessons: ["course-3/lesson-3-3", "course-3/lesson-4-9"],
              completedQuizzes: [],
              hasMergedLocal: false,
              mergedForUserId: null,
              pendingUpdates: [],
            },
            version: 0,
          }),
        );
        """
    )
    course = CourseMapPage(page, base_url)
    course.goto("/ru/course-3")
    course.open_lesson_node("course-3", "lesson-4-10")
    course.expect_url_path("/ru/course-3/block-4/lesson-4-10")
    expect(
        course.page.get_by_role("heading", name="Плитки и раскладка")
    ).to_be_visible()