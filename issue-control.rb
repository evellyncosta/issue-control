class Suacli < Formula
  desc "Issue control"
  homepage "https://github.com/evellyncosta/issue-control"
  url "https://github.com/seu-usuario/seu-repositorio/archive/v1.0.0.tar.gz"

  depends_on "python@3.9" #check compatibility later
  depends_on "gh"
  depends_on "setuptools" => :python

  def install
    bin.install "ic.py"
  end

  test do
    # Testes da CLI
  end
end
