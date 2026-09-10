#!/bin/sh
# Ensure course-* markdown trees exist under TARGET_DIR.
#
# Used by frontend/backend Dockerfiles when Railway watchPatterns or a narrow
# root directory omit course-* from the build archive. Prefers build-context
# copies; falls back to cloning the repo at build time.
set -eu

TARGET_DIR="${1:-/app}"
BUILD_CTX="${2:-/tmp/buildctx}"

mkdir -p "${TARGET_DIR}"

if [ -d "${BUILD_CTX}" ] && ls "${BUILD_CTX}"/course-[0-9]* >/dev/null 2>&1; then
  echo "Copying course-* from Docker build context into ${TARGET_DIR}..."
  cp -a "${BUILD_CTX}"/course-* "${TARGET_DIR}/"
fi

if ! ls "${TARGET_DIR}"/course-[0-9]* >/dev/null 2>&1; then
  GIT_REPO="${GIT_REPO:-https://github.com/asushko-AQA/PyCourse.git}"
  RAILWAY_GIT_BRANCH="${RAILWAY_GIT_BRANCH:-main}"
  RAILWAY_GIT_COMMIT_SHA="${RAILWAY_GIT_COMMIT_SHA:-}"

  echo "Build context has no course-* — fetching from ${GIT_REPO}..."
  apt-get update
  apt-get install -y --no-install-recommends git ca-certificates

  if [ -n "${RAILWAY_GIT_COMMIT_SHA}" ]; then
    git clone "${GIT_REPO}" /tmp/pycourse
    cd /tmp/pycourse
    git checkout "${RAILWAY_GIT_COMMIT_SHA}"
  else
    git clone --depth 1 --branch "${RAILWAY_GIT_BRANCH}" "${GIT_REPO}" /tmp/pycourse
  fi

  mv /tmp/pycourse/course-* "${TARGET_DIR}/"
  rm -rf /tmp/pycourse

  apt-get purge -y git
  apt-get autoremove -y
  rm -rf /var/lib/apt/lists/*
fi

if ! ls "${TARGET_DIR}"/course-[0-9]* >/dev/null 2>&1; then
  echo "ERROR: no course-* directories under ${TARGET_DIR}" >&2
  exit 1
fi

echo "Course content ready under ${TARGET_DIR}: $(ls -d "${TARGET_DIR}"/course-[0-9]* | tr '\n' ' ')"
