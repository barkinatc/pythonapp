# Minikube Cluster Oluşturma Dokümantasyonu (Linux Mint İçin)

Bu dokümantasyon, **Linux Mint** üzerinde **Minikube** yüklemesi ve **Minikube kümesi başlatma** adımlarını açıklamaktadır.

## 1. Minikube Yükleme (Linux Mint)

### 1.1. Gerekli Paketlerin Yüklenmesi

Minikube'u yüklemeden önce, Docker ve kubectl gibi gerekli paketlerin kurulu olması gerekiyor. Aşağıdaki adımları takip ederek gerekli paketleri yükleyebilirsiniz.

#### 1.1.1. Docker'ı Yükleme
Minikube, Docker sürücüsünü kullanarak küme başlatır, bu yüzden **Docker** kurulumunun yapılması gerekmektedir.

- Docker'ı yükleyin.

#### 1.1.2. Homebrew Yükleme
**Homebrew**, Linux üzerinde paketlerin kolayca yönetilmesini sağlayan bir araçtır. **Minikube**'u **Homebrew** kullanarak kolayca kurabilirsiniz. Aşağıda, **Linux Mint** üzerinde **Homebrew** ile **Minikube** kurulumunun adımlarını bulabilirsiniz.

### 2. Homebrew Yükleme

#### 2.1. Homebrew Yükleme

Homebrew'u yüklemek için terminale şu komutu yazın:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Kurulum tamamlandıktan sonra Homebrew sürümünü doğrulamak için şu komutu kullanabilirsiniz:

`brew --version`

#### 2.2. kubectl Yükleme (Homebrew ile)
Kubernetes komutlarını çalıştırabilmek için **kubectl**'in de yüklü olması gerekir.

- **kubectl** yüklemek için Homebrew kullanabilirsiniz:

`brew install kubectl`

---

## 3. Minikube Yükleme (Homebrew ile)

Homebrew kurulumunun ardından, **Minikube**'u yüklemek için şu komutu kullanabilirsiniz:

`brew install minikube`

Minikube yüklemesi tamamlandıktan sonra, Minikube kümesini başlatmak için şu komutu kullanabilirsiniz:

`minikube start`
