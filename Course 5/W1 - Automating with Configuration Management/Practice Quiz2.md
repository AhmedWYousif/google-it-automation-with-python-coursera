# Practice Quiz: Introduction to Puppet

### 1.A Puppet agent inspects /etc/conf.d, determines the OS to be Gentoo Linux, then activates the Portage package manager. What is the provider in this scenario?

    Portage

### 2.Which of the following examples show proper Puppet syntax?

```
class AutoConfig {
  package { 'Executable':
    ensure => latest,
  }
  file { 'executable.cfg':
    source => 'puppet:///modules/executable/Autoconfig/executable.cfg'
    replace => true,
  }
  service { 'executable.exe':
    enable  => true,
    ensure  => running,
  }
}
```

### 3.What is the benefit of grouping resources into classes when using Puppet?

    Configuration management is simplified

### 4.What defines which provider will be used for a particular resource?

    Puppet assigns providers based on the resource type and data collected from the system.

### 5.In Puppet’s file resource type, which attribute overwrites content that already exists?

    Replace
