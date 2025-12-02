class {{ cookiecutter.class_name }} < Formula
  include Language::Python::Virtualenv

  desc "{{ cookiecutter.project_short_description }}"
  homepage "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"
  url "https://files.pythonhosted.org/packages/PLACEHOLDER/{{ cookiecutter.package_name }}-0.1.0.tar.gz"
  sha256 "PLACEHOLDER_SHA256"
  license "{{ cookiecutter.license }}"

  depends_on "python@{{ cookiecutter.python_version }}"

  # Standard dependencies from cli-template
  resource "typer" do
    url "https://files.pythonhosted.org/packages/PLACEHOLDER/typer-VERSION.tar.gz"
    sha256 "PLACEHOLDER_SHA256_TYPER"
  end

  resource "rich" do
    url "https://files.pythonhosted.org/packages/PLACEHOLDER/rich-VERSION.tar.gz"
    sha256 "PLACEHOLDER_SHA256_RICH"
  end

  resource "click" do
    url "https://files.pythonhosted.org/packages/PLACEHOLDER/click-VERSION.tar.gz"
    sha256 "PLACEHOLDER_SHA256_CLICK"
  end

  resource "markdown-it-py" do
    url "https://files.pythonhosted.org/packages/PLACEHOLDER/markdown_it_py-VERSION.tar.gz"
    sha256 "PLACEHOLDER_SHA256_MARKDOWN_IT_PY"
  end

  resource "mdurl" do
    url "https://files.pythonhosted.org/packages/PLACEHOLDER/mdurl-VERSION.tar.gz"
    sha256 "PLACEHOLDER_SHA256_MDURL"
  end

  resource "pygments" do
    url "https://files.pythonhosted.org/packages/PLACEHOLDER/pygments-VERSION.tar.gz"
    sha256 "PLACEHOLDER_SHA256_PYGMENTS"
  end

  resource "shellingham" do
    url "https://files.pythonhosted.org/packages/PLACEHOLDER/shellingham-VERSION.tar.gz"
    sha256 "PLACEHOLDER_SHA256_SHELLINGHAM"
  end

  # Add additional project-specific dependencies here after first release

  def install
    virtualenv_install_with_resources
  end

  test do
    # Test version output
    output = shell_output("#{bin}/{{ cookiecutter.command_name }} --version")
    assert_match "{{ cookiecutter.command_name }} version", output

    # Test help output
    output = shell_output("#{bin}/{{ cookiecutter.command_name }} --help")
    assert_match "{{ cookiecutter.project_short_description }}", output
  end
end
